object Solution extends App {
  def runningSum(nums: Array[Int]): Array[Int] = {
    def inner(result: Array[Int], left: Seq[Int]): Array[Int] = {
      if (left.isEmpty) {
        result
      } else {
        inner(result ++ Seq(left.head), left.slice(0, left.length))
      }
    }
    inner(Array.empty[Int], nums)
  }
}
